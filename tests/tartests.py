#!/usr/bin/env python2
from __future__ import print_function

import os

from tests.tarfixtures    import TarFixtures
from tests.testenv        import TestEnvironment
from tests.testassertions import TestAssertions


class TarTestCases(TestEnvironment, TestAssertions):
    """Unit tests for 'tar'.

    tar-specific tests are in this class.  Other shared tests are
    included via the class inheritance hierarchy.
    """

    scm            = 'tar'
    fixtures_class = TarFixtures

    def test_tar_scm_finalize(self):
        wdir       = self.pkgdir
        info = os.path.join(wdir, "test.obsinfo")
        print("INFOFILE: '%s'" % info)
        os.chdir(self.pkgdir)
        obsinfo = open(info, 'w')
        obsinfo.write(
            "name: pkgname\n" +
            "version: 0.1.1\n" +
            "mtime: 1476683264\n" +
            "commit: fea6eb5f43841d57424843c591b6c8791367a9e5\n"
        )
        obsinfo.close()
        src_dir = os.path.join(wdir, "pkgname")
        os.mkdir(src_dir)
        self.tar_scm_std()
        self.assertTrue(os.path.isdir(src_dir))
