%define git_repo python-google-apputils
%define git_head HEAD

Summary:	Google Application Utilities for Python
Name:		python-google-apputils
Version:	%git_get_ver
Release:	%mkrel %git_get_rel2
Source:		%git_bs_source %{name}-%{version}.tar.gz
Source1:	%{name}-gitrpm.version
Source2:	%{name}-changelog.gitrpm.txt
License:	Apache
Group:		Development/Python
Url:		https://github.com/tonioo/sievelib
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	python-devel python-setuptools
Requires:       python-dateutil >= 1.4
Requires:       python-gflags >= 1.4
Requires:       python-pytz >= 2010

%description

This project is a small collection of utilities for building Python
applications.  It includes some of the same set of utilities used to build and
run internal Python apps at Google.

Features:

  * Simple application startup integrated with python-gflags.
  * Subcommands for command-line applications.
  * Option to drop into pdb on uncaught exceptions.
  * Helper functions for dealing with files.
  * High-level profiling tools.
  * Timezone-aware wrappers for datetime.datetime classes.
  * Improved TestCase with the same methods as unittest2, plus helpful flags for
    test startup.
  * google_test setuptools command for running tests.
  * Helper module for creating application stubs.


%prep
%git_get_source
%setup -q

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot} --record=FILE_LIST
# __rm -rf docs/_build/html/.buildinfo

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README LICENSE
%{python_sitelib}/google*.egg-info
%{python_sitelib}/google_apputils*.pth
%{python_sitelib}/google/apputils/*.py*
# %{python_sitelib}/sievelib/tests/*.py*

%changelog -f %{_sourcedir}/%{name}-changelog.gitrpm.txt
