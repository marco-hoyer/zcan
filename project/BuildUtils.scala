import sbt.ModuleID

object BuildUtils {

  def getVersion: String = scala.io.Source.fromFile("src/main/resources/version.conf").mkString.replace("app.version=", "").replaceAll("\\n", "")

  def cleanup(elems: ModuleID*): Seq[ModuleID] = elems.map(_
    .exclude("org.slf4j", "slf4j-log4j12")
    .exclude("log4j", "log4j")).toSeq
}

