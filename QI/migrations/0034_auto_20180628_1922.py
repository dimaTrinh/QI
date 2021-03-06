# Generated by Django 2.0.6 on 2018-06-28 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QI', '0033_auto_20180221_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affiliation',
            name='id_tei',
            field=models.CharField(max_length=50, verbose_name='TEI ID'),
        ),
        migrations.AlterField(
            model_name='location',
            name='id_tei',
            field=models.CharField(max_length=50, verbose_name='TEI ID'),
        ),
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Latitude'),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Longitude'),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Name of Place'),
        ),
        migrations.AlterField(
            model_name='loctype',
            name='id_tei',
            field=models.CharField(max_length=50, verbose_name='TEI ID'),
        ),
        migrations.AlterField(
            model_name='loctype',
            name='loc_type',
            field=models.CharField(blank=True, max_length=200, verbose_name='Name of Place'),
        ),
        migrations.AlterField(
            model_name='manuscript',
            name='call_no',
            field=models.CharField(blank=True, max_length=100, verbose_name='call_no'),
        ),
        migrations.AlterField(
            model_name='manuscript',
            name='date',
            field=models.CharField(blank=True, max_length=50, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='manuscript',
            name='id_tei',
            field=models.CharField(max_length=100, verbose_name='TEI ID'),
        ),
        migrations.AlterField(
            model_name='manuscript',
            name='location',
            field=models.CharField(blank=True, max_length=20, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='manuscript',
            name='org_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Organization'),
        ),
        migrations.AlterField(
            model_name='manuscript',
            name='person_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='manuscript',
            name='summary',
            field=models.CharField(blank=True, max_length=1000, verbose_name='summary'),
        ),
        migrations.AlterField(
            model_name='manuscript',
            name='title',
            field=models.CharField(blank=True, max_length=300, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='manuscript',
            name='transcribed',
            field=models.BooleanField(default=True, verbose_name='Transcribed'),
        ),
        migrations.AlterField(
            model_name='manuscript',
            name='type_of_Manuscript',
            field=models.CharField(blank=True, max_length=100, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='org',
            name='PYM_index',
            field=models.TextField(blank=True, max_length=500, verbose_name='PYM Index'),
        ),
        migrations.AlterField(
            model_name='org',
            name='associated_spellings',
            field=models.TextField(blank=True, max_length=500, verbose_name='Associated Spellings/Names'),
        ),
        migrations.AlterField(
            model_name='org',
            name='bio_notes',
            field=models.TextField(blank=True, max_length=500, verbose_name='Description Field'),
        ),
        migrations.AlterField(
            model_name='org',
            name='citations',
            field=models.TextField(blank=True, max_length=500, verbose_name='Description Field'),
        ),
        migrations.AlterField(
            model_name='org',
            name='data_notes',
            field=models.CharField(blank=True, max_length=500, verbose_name='LCNAF URI'),
        ),
        migrations.AlterField(
            model_name='org',
            name='date_dissolved',
            field=models.CharField(blank=True, max_length=500, verbose_name='Date Founded'),
        ),
        migrations.AlterField(
            model_name='org',
            name='date_founded',
            field=models.CharField(blank=True, max_length=500, verbose_name='Date Founded'),
        ),
        migrations.AlterField(
            model_name='org',
            name='id_tei',
            field=models.CharField(max_length=500, verbose_name='TEI ID'),
        ),
        migrations.AlterField(
            model_name='org',
            name='lcnaf_uri',
            field=models.CharField(blank=True, max_length=500, verbose_name='LCNAF URI'),
        ),
        migrations.AlterField(
            model_name='org',
            name='notes',
            field=models.CharField(blank=True, max_length=500, verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='org',
            name='org_type',
            field=models.CharField(blank=True, max_length=70, verbose_name='Oraganization Type'),
        ),
        migrations.AlterField(
            model_name='org',
            name='organization_name',
            field=models.CharField(blank=True, max_length=500, verbose_name='Name of Organization'),
        ),
        migrations.AlterField(
            model_name='org',
            name='other_names',
            field=models.CharField(blank=True, max_length=500, verbose_name='Other Names of Organization'),
        ),
        migrations.AlterField(
            model_name='page',
            name='fulltext',
            field=models.TextField(blank=True, verbose_name='Full Text'),
        ),
        migrations.AlterField(
            model_name='page',
            name='id_tei',
            field=models.CharField(max_length=50, verbose_name='TEI ID'),
        ),
        migrations.AlterField(
            model_name='page',
            name='img_url',
            field=models.CharField(blank=True, max_length=200, verbose_name='Image URL'),
        ),
        migrations.AlterField(
            model_name='page',
            name='transcribed',
            field=models.BooleanField(default=True, verbose_name='Transcribed'),
        ),
        migrations.AlterField(
            model_name='person',
            name='PYM_index',
            field=models.TextField(blank=True, max_length=100, verbose_name='PYM Index'),
        ),
        migrations.AlterField(
            model_name='person',
            name='affiliation1',
            field=models.CharField(blank=True, max_length=45, verbose_name='Affiliation 1'),
        ),
        migrations.AlterField(
            model_name='person',
            name='affiliation2',
            field=models.CharField(blank=True, max_length=45, verbose_name='Affiliation 2'),
        ),
        migrations.AlterField(
            model_name='person',
            name='bio_notes',
            field=models.TextField(blank=True, max_length=100, verbose_name='Biography Note Field'),
        ),
        migrations.AlterField(
            model_name='person',
            name='birth_date',
            field=models.CharField(blank=True, max_length=100, verbose_name='Birth Date'),
        ),
        migrations.AlterField(
            model_name='person',
            name='citations',
            field=models.TextField(blank=True, max_length=100, verbose_name='Citations'),
        ),
        migrations.AlterField(
            model_name='person',
            name='data_notes',
            field=models.TextField(blank=True, max_length=100, verbose_name='Data Note Field'),
        ),
        migrations.AlterField(
            model_name='person',
            name='death_date',
            field=models.CharField(blank=True, max_length=100, verbose_name='Death Date'),
        ),
        migrations.AlterField(
            model_name='person',
            name='display_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Display Name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(blank=True, max_length=20, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='person',
            name='id_tei',
            field=models.CharField(max_length=100, verbose_name='TEI ID'),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='lcnaf_uri',
            field=models.CharField(blank=True, max_length=100, verbose_name='URI LCNAF'),
        ),
        migrations.AlterField(
            model_name='person',
            name='middle_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Middle Name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='notes',
            field=models.TextField(blank=True, max_length=100, verbose_name='Note Field'),
        ),
        migrations.AlterField(
            model_name='person',
            name='other_names',
            field=models.TextField(blank=True, max_length=100, verbose_name='Other Names'),
        ),
        migrations.AlterField(
            model_name='person',
            name='review_status',
            field=models.CharField(max_length=100, verbose_name='TEI ID'),
        ),
        migrations.AlterField(
            model_name='place',
            name='alternate',
            field=models.TextField(blank=True, max_length=200, verbose_name='Alternate Names'),
        ),
        migrations.AlterField(
            model_name='place',
            name='county',
            field=models.CharField(blank=True, max_length=100, verbose_name='County'),
        ),
        migrations.AlterField(
            model_name='place',
            name='date',
            field=models.CharField(blank=True, max_length=100, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='place',
            name='id_tei',
            field=models.CharField(max_length=100, verbose_name='TEI ID'),
        ),
        migrations.AlterField(
            model_name='place',
            name='latitude',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Latitude'),
        ),
        migrations.AlterField(
            model_name='place',
            name='longitude',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Longitude'),
        ),
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Name of Place'),
        ),
        migrations.AlterField(
            model_name='place',
            name='notes',
            field=models.TextField(blank=True, max_length=500, verbose_name='Description Field'),
        ),
        migrations.AlterField(
            model_name='place',
            name='notes2',
            field=models.TextField(blank=True, max_length=500, verbose_name='Description Field'),
        ),
        migrations.AlterField(
            model_name='place',
            name='place_type',
            field=models.CharField(blank=True, choices=[('placeName', 'Place Name'), ('geogName', 'Geography Name')], default='placeName', max_length=30, verbose_name='Place Type'),
        ),
        migrations.AlterField(
            model_name='place',
            name='state',
            field=models.CharField(blank=True, max_length=100, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='id_tei',
            field=models.CharField(max_length=50, verbose_name='TEI ID'),
        ),
        migrations.AlterField(
            model_name='relationshiptype',
            name='id_tei',
            field=models.CharField(max_length=50, verbose_name='TEI ID'),
        ),
        migrations.AlterField(
            model_name='relationshiptype',
            name='relationship_type',
            field=models.CharField(blank=True, max_length=100, verbose_name='Relationship Type'),
        ),
        migrations.AlterField(
            model_name='roletype',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description of Role'),
        ),
        migrations.AlterField(
            model_name='roletype',
            name='role',
            field=models.CharField(blank=True, max_length=50, verbose_name='Role_Type'),
        ),
    ]
