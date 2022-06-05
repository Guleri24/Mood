name := "mood"
organization := "com.guleri24"

scalaVersion := "3.1.2"


// Set to false or remove if you want to show stubs as linking errors
nativeLinkStubs := true

enablePlugins(ScalaNativePlugin)

import scala.scalanative.build._

nativeConfig ~= {
  _.withLTO(LTO.thin)
    .withMode(Mode.releaseFast)
    .withGC(GC.commix)
}

