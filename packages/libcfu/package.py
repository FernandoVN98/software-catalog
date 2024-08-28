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
#     spack install libcfu
#
# You can edit this file again by typing:
#
#     spack edit libcfu
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Libcfu(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://downloads.sourceforge.net/project/libcfu/libcfu/libcfu-0.03/libcfu-0.03.tar.bz2?ts=gAAAAABmzu14m0wGhDN4LT4S4EDzC21VIsgTjwhZ-MdXyR8sMa3lmvQxc4leME_hwX0bZwjU1cov3b2iIvS3n2i226usAJrj8g%3D%3D"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    version("0.03", sha256="3ca322fb54a981aa84f75239b2f20a7def34eadbe7f30f7f7bd2f995ff713e7f")

    # FIXME: Add dependencies if required.
    # depends_on("foo")

    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args

    def setup_run_environment(self, env):
        env.set('LIBCFU', self.prefix)
