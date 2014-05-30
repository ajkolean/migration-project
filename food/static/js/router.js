Food.Router.map(function() {
    this.route("index", { path : "/"});
//    this.route("restaurants", {path : "/restaurants/:type"});
});

Food.IndexRoute = Ember.Route.extend({
    model: function() {
        //return this.store.find('Food');
       // return Food.Food.find();
       return Ember.$.getJSON('http://127.0.0.1:8000/index/');
    }
});

//Food.RestaurantsRoute = Ember.Route.extend({
//    model: function(params) {
//        return this.store.find('Restaurant', params.type);
//    },
//
//    serialize: function(restaurant) {
//        return {type: restaurant.get('type')};
//    }
//});


//Food.ApplicationRoute = Ember.Route.extend({
//    setupController: function(controller) {
//        controller.set('title', "Hello World!");
//    }
//});