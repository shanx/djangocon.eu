# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Day'
        db.create_table('schedule_day', (
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('schedule', ['Day'])

        # Adding model 'Slot'
        db.create_table('schedule_slot', (
            ('talk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['talks.Talk'])),
            ('length', self.gf('django.db.models.fields.IntegerField')(default=45)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('starttime', self.gf('django.db.models.fields.TimeField')()),
            ('day', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['schedule.Day'])),
        ))
        db.send_create_signal('schedule', ['Slot'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Day'
        db.delete_table('schedule_day')

        # Deleting model 'Slot'
        db.delete_table('schedule_slot')
    
    
    models = {
        'schedule.day': {
            'Meta': {'object_name': 'Day'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'schedule.slot': {
            'Meta': {'object_name': 'Slot'},
            'day': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schedule.Day']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.IntegerField', [], {'default': '45'}),
            'starttime': ('django.db.models.fields.TimeField', [], {}),
            'talk': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['talks.Talk']"})
        },
        'speakers.speaker': {
            'Meta': {'object_name': 'Speaker'},
            'biography': ('django.db.models.fields.TextField', [], {}),
            'bitbucket': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'github': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linkedin': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'organisation': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '100', 'blank': 'True'})
        },
        'talks.talk': {
            'Meta': {'object_name': 'Talk'},
            'abstract': ('django.db.models.fields.TextField', [], {}),
            'accepted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_index': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_index': 'True'}),
            'review_result': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'scheduled': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'speakers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'speakers'", 'symmetrical': 'False', 'to': "orm['speakers.Speaker']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }
    
    complete_apps = ['schedule']
