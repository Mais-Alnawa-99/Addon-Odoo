odoo.define('real_estate_management.property_website', function (require) {
    'use strict';

    var publicWidget = require('web.public.widget');
    var rpc = require('web.rpc');

    publicWidget.registry.PropertyView = publicWidget.Widget.extend({
        selector: '#property_container',
        events: {
            'click .property_action_buttons': '_viewDetails',
        },

        // Fetch property details and redirect to a detailed page
        _viewDetails: function (ev) {
            ev.preventDefault();
            var propertyId = $(ev.currentTarget).closest('.o_property_item').data('property_id');
            // Redirect to the property details page using the correct URL
            window.location = '/property/' + propertyId;
        },

        start: function () {
            var self = this;
            rpc.query({
                route: '/property/get_all',
            }).then(function (result) {
                self.$el.html(result);
            });
            return this._super.apply(this, arguments);
        }
    });
});
