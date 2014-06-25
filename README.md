# tar_scm (OBS source service) [![Build Status](https://travis-ci.org/openSUSE/obs-service-tar_scm.png?branch=master)](https://travis-ci.org/openSUSE/obs-service-tar_scm)

This is the git repository for [openSUSE:Tools/obs-service-tar_scm](https://build.opensuse.org/package/show/openSUSE:Tools/obs-service-tar_scm).
The authoritative source is:

* https://github.com/openSUSE/obs-service-tar_scm

The files in this top-level directory need to be installed using the following:

    mkdir -p /usr/lib/obs/service
    mkdir -p /etc/obs/services
    install -m 0755 tar_scm /usr/lib/obs/service
    install -m 0644 tar_scm.service /usr/lib/obs/service
    install -m 0644 tar_scm.rc /etc/obs/services/tar_scm

## Test suite

Run the test suite via:

    python tests/test.py

The output may become easier to understand if you uncomment the
'failfast' option in `test.py`.  This requires Python 2.7, however.
You may also find that the buffered `STDOUT` from test failures gets
displayed to the screen twice - once before the test failure (and
corresponding stacktrace), and once after; in which case just grep for
`/^FAIL: /` in the output and start reading from there.

If you want to narrow the tests being run, to speed up testing during
development, just temporarily tweak `test.py` as directed by the
comments.  In the future we should move to a better test framework
which provides a decent CLI whilst allowing flexibility over how the
test suite is built.  However it would still have to work on Python
2.6, for the benefit of older distributions such as SLE 11.

Note that for each test, a fresh `svn`/`git`/`hg`/`bzr` repository is
created, and `tar_scm` is invoked one *or more* times in a faked-up
OBS source service environment.  Whenever `tar_scm` invokes the VCS
for which its functionality is being tested, through modification of
`$PATH` it actually invokes `scm-wrapper`, which logs the VCS
invocation before continuing.

## Contributions

See the [CONTRIBUTING.md](CONTRIBUTING.md) file.
