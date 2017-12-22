import sbt.Keys.{name, _}

name := "zcan"

scalaVersion := "2.12.2"

version in ThisBuild := "0.0.0-SNAPSHOT"

lazy val root = (project in file("."))
  .enablePlugins(PlayScala)
  .disablePlugins(PlayLayoutPlugin)
  .enablePlugins(DockerPlugin)

packageOptions += Package.ManifestAttributes(
  "Implementation-Version" -> (version in ThisBuild).value,
  "Implementation-Title" -> name.value
)

libraryDependencies ++= Seq(
  "org.slf4j" % "log4j-over-slf4j" % "1.7.12",
  "org.slf4j" % "jcl-over-slf4j" % "1.7.12",
  "org.scalaz" %% "scalaz-core" % "7.2.14",
  "com.softwaremill.macwire" %% "macros" % "2.3.0" % "provided",
  "com.softwaremill.macwire" %% "util" % "2.3.0",
  "com.amazonaws" % "aws-java-sdk" % "1.11.70",
  "com.amazonaws" % "aws-java-sdk-core" % "1.11.70",
  "org.apache.commons" % "commons-lang3" % "3.5",
  "com.typesafe.akka" %% "akka-testkit" % "2.4.17" % "test",
  "com.typesafe.akka" %% "akka-stream-testkit" % "2.4.17" % "test",
  "org.mockito" % "mockito-all" % "1.9.5" % "test",
  "ch.jodersky" %% "akka-serial-core" % "4.1.2"
)

daemonUser := "daemonuser"

maintainer in Docker := "marco_hoyer@gmx.de"

dockerBaseImage := "anapsix/alpine-java:8"

dockerExposedPorts += 9000

dockerUpdateLatest := false

scalacOptions ++= Seq("-feature", "-language:postfixOps", "-target:jvm-1.8")

javaOptions in Test ++= Seq("-Dconfig.resource=test-application.conf", "-Xmx1024M")

javaOptions in run ++= Seq("-Dlogger.resource=local-logback.xml", "-Xmx1024M")

javacOptions in Compile ++= Seq("-source", "1.8", "-target", "1.8")

sources in(Compile, doc) := Seq.empty

publishArtifact in(Compile, packageDoc) := false

lazy val osName = settingKey[Option[String]]("OS Name")

osName := {
  sys.props.get("os.name")
}

//fork in Test := false

