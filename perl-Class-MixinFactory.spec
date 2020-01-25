#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Class
%define		pnam	MixinFactory
Summary:	Class::MixinFactory - class factory with selection of mixins
Summary(pl.UTF-8):	Class::MixinFactory - tworzenie klas z wyborem klas towarzyskich
Name:		perl-Class-MixinFactory
Version:	0.92
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	577d76cdc3c5b0c313634f783c96c767
URL:		http://search.cpan.org/dist/Class-MixinFactory/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This distribution facilitates the run-time generation of classes which
inherit from a base class and some optional selection of mixin
classes.

A factory is provided to generate the mixed classes with multiple
inheritance. A NEXT method allows method redispatch up the inheritance
chain.

%description -l pl.UTF-8
Ten pakiet ułatwia generowanie w czasie działania programu klas
dziedziczących z klasy bazowej i pewnego opcjonalnego wyboru klas
towarzyskich (mixin).

Udostępniony jest generator do tworzenia klas mieszanych z
wielokrotnym dziedziczeniem. Metoda NEXT umożliwia wysyłanie metod po
łańcuchu dziedziczenia.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES
%{perl_vendorlib}/Class/MixinFactory.pm
%{perl_vendorlib}/Class/MixinFactory
%{_mandir}/man3/*
