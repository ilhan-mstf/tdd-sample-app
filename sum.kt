fun main(args: Array<String>) {
  if (args.size < 1) {
    println("Error! Please provide at least one integer number")
    return
  }
  val numbers: List<Int> = args.map { it.toInt() }
  println(numbers.sum())
}