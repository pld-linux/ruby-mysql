%define	ruby_sitearchdir	%(ruby -r rbconfig -e 'print Config::CONFIG["sitearchdir"]')
%define tarname mysql-ruby
Summary:	MySQL module for Ruby
Summary(pl):	Modu³ MySQL dla Ruby
Name:		ruby-mysql
Version:	2.4.2
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://www.tmtm.org/mysql/ruby/%{tarname}-%{version}.tar.gz
URL:		http://www.tmtm.org/mysql/ruby/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	ruby
BuildRequires:	mysql-devel
Requires:	ruby

%description
MySQL module for Ruby.

%description -l pl
Modu³ MySQL dla Ruby.

%prep
%setup -q -n %{tarname}-%{version}

%build
ruby extconf.rb --with-mysql-dir=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{ruby_sitearchdir}

%{__make} archdir=$RPM_BUILD_ROOT/%{ruby_sitearchdir} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%{ruby_sitearchdir}/*
