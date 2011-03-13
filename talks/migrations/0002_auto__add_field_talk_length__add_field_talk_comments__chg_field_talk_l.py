# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Talk.length'
        db.add_column('talks_talk', 'length', self.gf('django.db.models.fields.CharField')(default='long', max_length=20, db_index=True), keep_default=False)

        # Adding field 'Talk.comments'
        db.add_column('talks_talk', 'comments', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Changing field 'Talk.level'
        db.alter_column('talks_talk', 'level', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Adding index on 'Talk', fields ['level']
        db.create_index('talks_talk', ['level'])


    def backwards(self, orm):
        
        # Removing index on 'Talk', fields ['level']
        db.delete_index('talks_talk', ['level'])

        # Deleting field 'Talk.length'
        db.delete_column('talks_talk', 'length')

        # Deleting field 'Talk.comments'
        db.delete_column('talks_talk', 'comments')

        # Changing field 'Talk.level'
        db.alter_column('talks_talk', 'level', self.gf('django.db.models.fields.PositiveSmallIntegerField')())


    models = {
        'speakers.speaker': {
            'Meta': {'object_name': 'Speaker'},
            'biography': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
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
            'accepted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_index': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_index': 'True'}),
            'scheduled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'speakers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'speakers'", 'symmetrical': 'False', 'to': "orm['speakers.Speaker']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['talks']
