name := "mood"
organization := "com.guleri24"

scalaVersion := "3.1.2"

// https://mvnrepository.com/artifact/org.rogach/scallop
libraryDependencies += "org.rogach" % "scallop_native0.4_2.13" % "4.1.0"

// Set to false or remove if you want to show stubs as linking errors
nativeLinkStubs := true

enablePlugins(ScalaNativePlugin)

import scala.scalanative.build._

nativeConfig ~= {
  _.withLTO(LTO.thin)
    .withMode(Mode.releaseFast)
    .withGC(GC.commix)
}

