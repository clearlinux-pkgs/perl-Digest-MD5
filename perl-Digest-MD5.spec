#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Digest-MD5
Version  : 2.55
Release  : 10
URL      : http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/Digest-MD5-2.55.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/Digest-MD5-2.55.tar.gz
Summary  : 'Perl interface to the MD-5 algorithm'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Digest-MD5-lib = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
The Digest::MD5 module allows you to use the RSA Data Security
Inc. MD5 Message Digest algorithm from within Perl programs.  The
algorithm takes as input a message of arbitrary length and produces as
output a 128-bit "fingerprint" or "message digest" of the input.
MD5 is described in RFC 1321.

%package dev
Summary: dev components for the perl-Digest-MD5 package.
Group: Development
Requires: perl-Digest-MD5-lib = %{version}-%{release}
Provides: perl-Digest-MD5-devel = %{version}-%{release}

%description dev
dev components for the perl-Digest-MD5 package.


%package lib
Summary: lib components for the perl-Digest-MD5 package.
Group: Libraries

%description lib
lib components for the perl-Digest-MD5 package.


%prep
%setup -q -n Digest-MD5-2.55

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/x86_64-linux-thread-multi/Digest/MD5.pm

%files dev
%defattr(-,root,root,-)
%exclude /usr/share/man/man3/Digest::MD5.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/x86_64-linux-thread-multi/auto/Digest/MD5/MD5.so
