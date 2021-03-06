// Generated by CoffeeScript 1.6.3
(function() {
  var Animal, Invertebrate, mwoar, tiger, _ref,
    __bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; },
    __hasProp = {}.hasOwnProperty,
    __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; };

  Animal = (function() {
    function Animal(name) {
      this.name = name;
      this.roar = __bind(this.roar, this);
    }

    Animal.prototype.roar = function() {
      return console.log("I am a " + this.name + ", hear me roar!");
    };

    Animal.prototype.roar2 = function() {
      return console.log("Am I a " + this.name + "?");
    };

    Animal.find = function() {
      return console.log("Looking for an Animal");
    };

    return Animal;

  })();

  Invertebrate = (function(_super) {
    __extends(Invertebrate, _super);

    function Invertebrate() {
      this.roar = __bind(this.roar, this);
      _ref = Invertebrate.__super__.constructor.apply(this, arguments);
      return _ref;
    }

    Invertebrate.prototype.roar = function() {
      return console.log("Hsss, hsss " + this.name + ", hsss hsss hsss!");
    };

    return Invertebrate;

  })(Animal);

  tiger = new Invertebrate("tiger");

  tiger.roar2();

  mwoar = tiger.roar2;

  mwoar();

}).call(this);
