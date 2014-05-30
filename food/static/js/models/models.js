Food.Food = DS.Model.extend({
    type: DS.attr('string'),
    country: DS.attr('string'),
    healthiness: DS.attr('number')
});

Food.Restaurant = DS.Model.extend({
    name: DS.attr('string'),
    type: DS.attr('string'),
    daysopen: DS.attr('string'),
    location: DS.attr('string'),
    derrscore: DS.attr('number'),
    website: DS.attr('string')
});

