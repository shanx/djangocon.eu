# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Speaker.organisation'
        db.add_column('speakers_speaker', 'organisation', self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True), keep_default=False)

        # Adding field 'Speaker.linkedin'
        db.add_column('speakers_speaker', 'linkedin', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True), keep_default=False)

        # Adding field 'Speaker.biography'
        db.add_column('speakers_speaker', 'biography', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Changing field 'Speaker.website'
        db.alter_column('speakers_speaker', 'website', self.gf('django.db.models.fields.URLField')(max_length=100))

        # Changing field 'Speaker.twitter'
        db.alter_column('speakers_speaker', 'twitter', self.gf('django.db.models.fields.CharField')(max_length=100))


    def backwards(self, orm):
        
        # Deleting field 'Speaker.organisation'
        db.delete_column('speakers_speaker', 'organisation')

        # Deleting field 'Speaker.linkedin'
        db.delete_column('speakers_speaker', 'linkedin')

        # Deleting field 'Speaker.biography'
        db.delete_column('speakers_speaker', 'biography')

        # Changing field 'Speaker.website'
        db.alter_column('speakers_speaker', 'website', self.gf('django.db.models.fields.URLField')(max_length=200))

        # Changing field 'Speaker.twitter'
        db.alter_column('speakers_speaker', 'twitter', self.gf('django.db.models.fields.CharField')(max_length=75))


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
        }
    }

    complete_apps = ['speakers']
