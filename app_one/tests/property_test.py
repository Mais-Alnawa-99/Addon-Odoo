from odoo.tests.common import TransactionCase

class PropertyTest(TransactionCase):
    def setUp(self, *args, **kwargs):

     super(PropertyTest, self).setUp()
     self.property_record = self.env['property'].create({
         'name': 'prop',
         'postcode': "1234",
     })

    def test_property(self):
        property_id = self.property_record
        self.assertRecordValues(property_id, [
            {
                'name': 'prop',
                'postcode': "1234",
            }
        ])