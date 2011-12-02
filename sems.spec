#
Summary:	Media and application server for SIP based VoIP services
Summary(pl.UTF-8):	Serwer mediów i aplikacji dla usług VoIP
Name:		sems
Version:	1.4.2
Release:	0.1
License:	GPL v2+
Group:		Networking/Daemons
Source0:	http://ftp.iptel.org/pub/sems/%{name}-%{version}.tar.gz
# Source0-md5:	6c3fb1330df6690404565220f5115d61
#Source1:	-
URL:		http://http://www.iptel.org/sems
BuildRequires:	rpmbuild(macros) >= 1.228
Requires(post,preun):	/sbin/chkconfig
Requires:		rc-scripts
BuildRequires:	python-devel
BuildRequires:	flite-devel
BuildRequires:	lame-libs-devel
BuildRequires:	spandsp-devel
BuildRequires:	libev-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SEMS is a media and application server for SIP based VoIP services. It
shows good performance doing basic services like announcements and
conference for combination with external application servers, and,
thanks to its easy to use and flexible application development
framework and back-to-back user agent support, application logic and
media serving can be combined in the same process.

%description -l pl.UTF-8
SEMS to serwer mediów i aplikacji dla usług VoIP opartych o protokół
SIP.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{sysconfig,rc.d/init.d}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add %{name}
%service %{name} restart

%preun
if [ "$1" = "0" ]; then
	%service -q %{name} stop
	/sbin/chkconfig --del %{name}
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS CHANGES ChangeLog NEWS README THANKS TODO

%if 0
# if _sysconfdir != /etc:
#%%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/%{name}*
%{_datadir}/%{name}
%endif

%attr(754,root,root) /etc/rc.d/init.d/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
