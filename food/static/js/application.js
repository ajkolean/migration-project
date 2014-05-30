Food = Ember.Application.create();


Food.Store = DS.Store.extend({
    revision: 12,
    adapter: DS.DjangoRESTAdapter.create({
        namespace:  'Food'
    })
});



