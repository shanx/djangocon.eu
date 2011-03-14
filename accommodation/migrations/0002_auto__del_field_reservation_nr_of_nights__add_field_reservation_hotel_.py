# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Reservation.nr_of_nights'
        db.delete_column('accommodation_reservation', 'nr_of_nights')

        # Adding field 'Reservation.hotel_alternative'
        db.add_column('accommodation_reservation', 'hotel_alternative', self.gf('django.db.models.fields.related.ForeignKey')(related_name='alternative_set', null=True, to=orm['accommodation.Hotel']), keep_default=False)

        # Changing field 'Reservation.email_address'
        db.alter_column('accommodation_reservation', 'email_address', self.gf('django.db.models.fields.EmailField')(max_length=50))


    def backwards(self, orm):
        
        # User chose to not deal with backwards NULL issues for 'Reservation.nr_of_nights'
        raise RuntimeError("Cannot reverse this migration. 'Reservation.nr_of_nights' and its values cannot be restored.")

        # Deleting field 'Reservation.hotel_alternative'
        db.delete_column('accommodation_reservation', 'hotel_alternative_id')

        # Changing field 'Reservation.email_address'
        db.alter_column('accommodation_reservation', 'email_address', self.gf('django.db.models.fields.CharField')(max_length=50))


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
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            'hotel': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reservation_set'", 'to': "orm['accommodation.Hotel']"}),
            'hotel_alternative': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'alternative_set'", 'null': 'True', 'to': "orm['accommodation.Hotel']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initials': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'name_second_guest': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'nr_of_guests': ('django.db.models.fields.IntegerField', [], {}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'town': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['accommodation']
