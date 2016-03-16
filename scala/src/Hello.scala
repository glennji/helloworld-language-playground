/**
 * Created by gmason on 27/05/15.
 */
object Hello {
  def main(args: Array[String]): Unit = {
    val name = args.mkString("; ")
    println(s"Hello $name")
  }

  def max(x: Int, y: Int): Int = {
    return if (x > y) x else y
  }
}


