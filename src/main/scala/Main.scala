import java.nio.charset.Charset
import scalanative.unsafe.*
import scala.io.Source.fromFile
import scala.collection.mutable.Map
import scala.io.StdIn.readLine


@extern
object os_call {
  def exec(s: CString): Unit = extern

  def input(): CString = extern
}


object Main {

  def main(args: Array[String]): Unit = {
    import os_call._

    val states = collection.mutable.Map("info" -> c"cat logo.txt")
    val command: String = readLine()

    if (states.contains(command)) {
      val execCmd: CString = states.getOrElse(command, c"ls")
      exec(execCmd)
    } else
      exec(c"dir")
  }
}


