import scalanative.unsafe._

@extern
object oscall {
  def exec(s: CString): Unit = extern

  def input(): CString = extern
}


object Main {

  def main(args: Array[String]): Unit = {
    import oscall._
    val command: CString = input()
    exec(command)
  }
}


