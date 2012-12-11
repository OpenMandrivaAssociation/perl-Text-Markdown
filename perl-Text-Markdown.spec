%define upstream_name    Text-Markdown
%define upstream_version 1.000031

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Convert Markdown syntax to (X)HTML
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(Encode)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Slurp)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Text::Balanced)

BuildArch:	noarch

%description
Markdown is a text-to-HTML filter; it translates an easy-to-read /
easy-to-write structured text format into HTML. Markdown's text format is
most similar to that of plain text email, and supports features such as
headers, *emphasis*, code blocks, blockquotes, and links.

Markdown's syntax is designed not as a generic markup language, but
specifically to serve as a front-end to (X)HTML. You can use span-level
HTML tags anywhere in a Markdown document, and you can use block level HTML
tags (like <div> and <table> as well).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.0.31-2mdv2011.0
+ Revision: 655234
- rebuild for updated spec-helper

* Mon Mar 22 2010 Jérôme Quelin <jquelin@mandriva.org> 1.0.31-1mdv2011.0
+ Revision: 526463
- update to 1.000031

* Tue Jan 19 2010 Jérôme Quelin <jquelin@mandriva.org> 1.0.30-1mdv2010.1
+ Revision: 493489
- update to 1.000030

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.0.29-1mdv2010.1
+ Revision: 471156
- import perl-Text-Markdown


* Sun Nov 29 2009 cpan2dist 1.000029-1mdv
- initial mdv release, generated with cpan2dist
