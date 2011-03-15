# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Reservation'
        db.delete_table('accommodation_reservation')


    def backwards(self, orm):
        
        # Adding model 'Reservation'
        db.create_table('accommodation_reservation', (
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('town', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('arrival_date', self.gf('django.db.models.fields.DateField')()),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('name_second_guest', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('hotel', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reservation_set', to=orm['accommodation.Hotel'])),
            ('nr_of_guests', self.gf('django.db.models.fields.IntegerField')()),
            ('company_name', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('departure_date', self.gf('django.db.models.fields.DateField')()),
            ('initials', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('email_address', self.gf('django.db.models.fields.EmailField')(max_length=50)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hotel_alternative', self.gf('django.db.models.fields.related.ForeignKey')(related_name='alternative_set', null=True, to=orm['accommodation.Hotel'])),
        ))
        db.send_create_signal('accommodation', ['Reservation'])


    models = {
        'accommodation.hotel': {
            'Meta': {'ordering': "['nr_of_stars', 'name']", 'object_name': 'Hotel'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'breakfast': ('django.db.models.fields.TextField', [], {}),
            'cancellation_policy': ('django.db.models.fields.TextField', [], {}),
            'city_tax': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'date_available': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nr_of_stars': ('django.db.models.fields.IntegerField', [], {}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'rate_double': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'rate_single': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'wifi': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['accommodation']
