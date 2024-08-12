# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install cybershake
#
# You can edit this file again by typing:
#
#     spack edit cybershake
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *
import os


class Cybershake(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/SCECcode/cybershake-core/archive/refs/tags/study_22_12_v2.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    version("22_12_v2", sha256="6b5d73addd9713b61b52790381db9d284b42fc62b9135d17cd5fd0c0980ab0be")


    patch("makefile.patch")
    patch("makefile_sgthead.patch")
    patch("directsynth.patch")

    # FIXME: Add dependencies if required.
    depends_on("openmpi")

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        mkdirp(self.prefix.bin)
        with open("install.sh", "w") as f:
            f.write("#!/bin/sh\n"
            "cd ./AWP-ODC-SGT\n"
            "mkdir ./bin\n"
            "cd ./src\n"
            "make")
        f.close()
        os.system("chmod 755 ./install.sh")
        with open("compile_getpar.sh", "w") as f:
            f.write("#!/bin/sh\n"
                    "cd ./Getpar/getpar\n"
                    "mkdir ./lib\n"
                    "cd ./src\n"
                    "make")
        f.close()
        os.system("chmod 755 ./compile_getpar.sh")
        install_script = Executable('./compile_getpar.sh')
        install_script()
        install(os.getcwd() + "/Getpar/getpar/src/libget.a", self.prefix.bin)
        with open("install_sgthead.sh", "w") as f:
            f.write("#!/bin/sh\n"
            "cd ./SgtHead\n"
            "mkdir ./bin\n"
            "cd ./src\n"
            "make")
        f.close()
        os.system("chmod 755 ./install_sgthead.sh")
        install_script = Executable('./install.sh')
        install_script()
        with open("compile_rupgen.sh", "w") as f:
            f.write("#!/bin/sh\n"
                    "cd ./RuptureCodes\n"
                    "cd ./RupGen-api-5.5.2\n"
                    "mkdir ./lib\n"
                    "cd ./src\n"
                    "make")
        f.close()
        os.system("chmod 755 ./compile_rupgen.sh")
        with open("install_directsynth.sh", "w") as f:
            f.write("#!/bin/sh\n"
                "cd ./DirectSynth\n"
                "mkdir ./bin\n"
                "cd ./src\n"
                "make")
        f.close()
        #binom_jar, _ = urlretrieve(
        #    "https://b2drop.bsc.es/index.php/s/SRWPNAkKL73oaRw/download",
        #    filename="BINOM.jar",
        #)
        os.system("chmod 755 ./install_directsynth.sh")
        install(os.getcwd() + '/AWP-ODC-SGT/bin/pmcl3d', self.prefix.bin)
        install_script = Executable('./install_sgthead.sh')
        install_script()
        install_script = Executable('./compile_rupgen.sh')
        install_script()
        install(os.getcwd() + '/RuptureCodes/RupGen-api-5.5.2/src/librupgen.a', self.prefix.bin)
        install_script = Executable('./install_directsynth.sh')
        install_script()
        install(os.getcwd() + '/SgtHead/bin/*', self.prefix.bin)
        install(os.getcwd() + '/DirectSynth/bin/*', self.prefix.bin)

