var App = Ember.Application.create();

App.Router.map(function() {
    this.resource("foods", function() {
        this.route("restaurants", { path : "/restaurants/:restaurant_id" });
    });
   // this.resource("food", { path: ':/food_id' });
//    this.route("restaurants", {path : "/restaurants/:type"});
});

App.IndexController = Ember.Controller.extend({

});

App.ApplicationAdapter = DS.RESTAdapter.extend({
        defaultSerializer: 'django'
});


App.Food = DS.Model.extend({

    type: DS.attr('string'),
    country: DS.attr('string'),
    healthiness: DS.attr('number'),
    restaurants: DS.hasMany('restaurant')
});

App.Restaurant = DS.Model.extend({
    name: DS.attr('string'),
    type: DS.attr('string'),
    daysopen: DS.attr('string'),
    location: DS.attr('string'),
    derrscore: DS.attr('number'),
    website: DS.attr('string'),
    food: DS.belongsTo('food')
});





App.FoodsRoute = Ember.Route.extend({
    model: function() {
    //console.log(this.store.find('food'));
    return this.store.find('food');
    //return Ember.$.getJSON('http://127.0.0.1:8000/foods');
     //console.log(App.Food.find(1));
    // return Ember.$.getJSON('https://api.clever.com/v1.1/students/530e5960049e75a9262cff1d');
    }
});

//App.FoodRoute = Ember.Controller.extend({
//    model: function(params) {
//        return this.store.find('food', params.food_id);
//    }
//});