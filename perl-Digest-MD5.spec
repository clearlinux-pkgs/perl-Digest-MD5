#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Digest-MD5
Version  : 2.58
Release  : 24
URL      : https://cpan.metacpan.org/authors/id/T/TO/TODDR/Digest-MD5-2.58.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TO/TODDR/Digest-MD5-2.58.tar.gz
Summary  : 'Perl interface to the MD-5 algorithm'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Digest-MD5-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
The Digest::MD5 module allows you to use the RSA Data Security
Inc. MD5 Message Digest algorithm from within Perl programs.  The
algorithm takes as input a message of arbitrary length and produces as
output a 128-bit "fingerprint" or "message digest" of the input.
MD5 is described in RFC 1321.

%package perl
Summary: perl components for the perl-Digest-MD5 package.
Group: Default
Requires: perl-Digest-MD5 = %{version}-%{release}

%description perl
perl components for the perl-Digest-MD5 package.


%prep
%setup -q -n Digest-MD5-2.58
cd %{_builddir}/Digest-MD5-2.58

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
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
## Remove excluded files
rm -f %{buildroot}/usr/share/man/man3/Digest::MD5.3

%files
%defattr(-,root,root,-)

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/x86_64-linux-thread-multi/Digest/MD5.pm
/usr/lib/perl5/vendor_perl/5.30.3/x86_64-linux-thread-multi/auto/Digest/MD5/MD5.so
