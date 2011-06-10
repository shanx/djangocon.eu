# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Slides'
        db.create_table('talks_slides', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('talks', ['Slides'])

        # Adding field 'Talk.video'
        db.add_column('talks_talk', 'video', self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True), keep_default=False)

        # Adding M2M table for field slides on 'Talk'
        db.create_table('talks_talk_slides', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('talk', models.ForeignKey(orm['talks.talk'], null=False)),
            ('slides', models.ForeignKey(orm['talks.slides'], null=False))
        ))
        db.create_unique('talks_talk_slides', ['talk_id', 'slides_id'])

        # Adding field 'LightningTalk.slides'
        db.add_column('talks_lightningtalk', 'slides', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['talks.Slides'], null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'Slides'
        db.delete_table('talks_slides')

        # Deleting field 'Talk.video'
        db.delete_column('talks_talk', 'video')

        # Removing M2M table for field slides on 'Talk'
        db.delete_table('talks_talk_slides')

        # Deleting field 'LightningTalk.slides'
        db.delete_column('talks_lightningtalk', 'slides_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
            'notified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'organisation': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '100', 'blank': 'True'})
        },
        'talks.lightningtalk': {
            'Meta': {'object_name': 'LightningTalk'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slides': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['talks.Slides']", 'null': 'True', 'blank': 'True'}),
            'speaker_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'speaker_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'talk_title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'talks.review': {
            'Meta': {'unique_together': "(('talk', 'voter'),)", 'object_name': 'Review'},
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'talk': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['talks.Talk']"}),
            'vote': ('django.db.models.fields.IntegerField', [], {}),
            'voter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'talks.slides': {
            'Meta': {'object_name': 'Slides'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
            'review_result': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'scheduled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slides': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['talks.Slides']", 'symmetrical': 'False'}),
            'speakers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['speakers.Speaker']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'video': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['talks']
