class Animal
	constructor: (@name) ->
	roar: =>
		console.log  "I am a #{@name}, hear me roar!"
	roar2: ->
		console.log "Am I a #{@name}?"
	# How about a static method? 
	@find: ->
		console.log "Looking for an Animal"

class Invertebrate extends Animal
	roar: =>
		console.log "Hsss, hsss #{@name}, hsss hsss hsss!"


tiger = new Invertebrate("tiger")
tiger.roar2()

mwoar = tiger.roar2

mwoar()