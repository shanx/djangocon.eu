# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Hotel'
        db.create_table('accommodation_hotel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('nr_of_stars', self.gf('django.db.models.fields.IntegerField')()),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('place', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('rate_single', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('rate_double', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('city_tax', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('breakfast', self.gf('django.db.models.fields.TextField')()),
            ('wifi', self.gf('django.db.models.fields.TextField')()),
            ('cancellation_policy', self.gf('django.db.models.fields.TextField')()),
            ('date_available', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('accommodation', ['Hotel'])

        # Adding model 'Reservation'
        db.create_table('accommodation_reservation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hotel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accommodation.Hotel'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('initials', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('company_name', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('town', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email_address', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('arrival_date', self.gf('django.db.models.fields.DateField')()),
            ('departure_date', self.gf('django.db.models.fields.DateField')()),
            ('nr_of_nights', self.gf('django.db.models.fields.IntegerField')()),
            ('nr_of_guests', self.gf('django.db.models.fields.IntegerField')()),
            ('name_second_guest', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('accommodation', ['Reservation'])


    def backwards(self, orm):
        
        # Deleting model 'Hotel'
        db.delete_table('accommodation_hotel')

        # Deleting model 'Reservation'
        db.delete_table('accommodation_reservation')


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
        },
        'accommodation.reservation': {
            'Meta': {'object_name': 'Reservation'},
            'arrival_date': ('django.db.models.fields.DateField', [], {}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'departure_date': ('django.db.models.fields.DateField', [], {}),
            'email_address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'hotel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accommodation.Hotel']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initials': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'name_second_guest': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'nr_of_guests': ('django.db.models.fields.IntegerField', [], {}),
            'nr_of_nights': ('django.db.models.fields.IntegerField', [], {}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'town': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['accommodation']
