%define tarname mysql-ruby
Summary:	MySQL module for Ruby
Summary(pl):	Modu³ MySQL dla Ruby
Name:		ruby-mysql
Version:	2.4.2
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://www.tmtm.org/mysql/ruby/mysql-ruby-%{version}.tar.gz
URL:		http://www.tmtm.org/mysql/ruby/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	ruby, mysql, mysql-devel
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
archdir=`ruby -r rbconfig -e 'p Config::CONFIG["archdir"]'`
install -d $RPM_BUILD_ROOT/$archdir

%{__make} archdir=$RPM_BUILD_ROOT/$archdir install

find $RPM_BUILD_ROOT%{_prefix} -type f -print | sed -e "s@^$RPM_BUILD_ROOT@@g" > %{name}-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-filelist
%defattr(644,root,root,755)
%doc README*
