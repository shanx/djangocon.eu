# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'WaitList'
        db.create_table('waitlist_waitlist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('organisation', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('ticket_type', self.gf('django.db.models.fields.CharField')(max_length=20, db_index=True)),
            ('nr_tickets', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('waitlist', ['WaitList'])


    def backwards(self, orm):
        
        # Deleting model 'WaitList'
        db.delete_table('waitlist_waitlist')


    models = {
        'waitlist.waitlist': {
            'Meta': {'object_name': 'WaitList'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'nr_tickets': ('django.db.models.fields.IntegerField', [], {}),
            'organisation': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'ticket_type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_index': 'True'})
        }
    }

    complete_apps = ['waitlist']
