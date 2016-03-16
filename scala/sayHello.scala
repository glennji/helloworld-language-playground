/**
 * Created by gmason on 27/05/15.
 */
Hello.main(Array("Bob", "Neven"))

println(Hello.max(4, 5))
println(Hello.max(3e5.toInt, 5))


val name = "BobISGreat"
val x = name.filter(x => x.isUpper)
println(x)

for (i <- 0 to name.length - 1) {
  println(name(i))
}

val una = List(1)
val duo = List(2)
val numero = una ::: duo

println(numero)
// numero(0) = "faaaaaaaaa...."
//println(numero._0)
//numero._1 = 3
//println(numero)


//var y = 1
//def scopey(y: Int) = {
//  y = 2
//}

SumAccumulator a = new SumAccumulator()