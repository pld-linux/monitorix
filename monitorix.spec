# TODO
# - /usr/share isn't proper place for %config files
# - kill /home/services
# - kill defattr(-,...)
# - missing dirs
# - webapps integration
Summary:	Lightweight system monitoring tool to monitorize as many services as it can
Summary(pl):	Lekkie narzêdzie do monitorowania jak najwiêkszej liczby us³ug w systemie
Name:		monitorix
Version:	0.8.1
Release:	0.2
License:	GPL
Group:		Applications/System
Source0:	http://www.monitorix.org/%{name}-%{version}.tar.gz
# Source0-md5:	ddd330c84b59ea7ebb7cf63d9031757f
Source1:	%{name}.conf
URL:		http://www.monitorix.org/
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	bash
Requires:	perl-rrdtool
Requires:	rc-scripts
Requires:	rrdtool
Requires:	webserver
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/%{name}
%define		_webapps	/etc/webapps
%define		_webapp		%{name}
%define		_sysconfdir	%{_webapps}/%{_webapp}

%description
Monitorix is a free, open source, lightweight system monitoring tool
designed to monitorize as many services as it can. At this time it
monitors from the CPU load and temperatures to the users using the
system. Network devices activity, network services demand and even the
devices' interrupt activity are also monitored.

%description -l pl
Monitorix to wolnodostêpne i maj±ce otwarte ¼ród³a lekkie narzêdzie
do monitorowania systemu zaprojektowane do monitorowania jak
najwiêkszej liczby us³ug. Aktualnie ¶ledzi parametry od obci±¿enia
procesora i temperatur do u¿ytkowników korzystaj±cych z systemu.
Monitorowane s± tak¿e ¿±dania us³ug sieciowych, aktywno¶æ interfejsów
sieciowych, a nawet aktywno¶æ przerwañ urz±dzeñ.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/rc.d/init.d
install ports/Linux-RHFC/monitorix.init $RPM_BUILD_ROOT/etc/rc.d/init.d/monitorix
install -d $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d
install monitorix-apache.conf $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/monitorix.conf
install -d $RPM_BUILD_ROOT%{_sysconfdir}
install monitorix.conf $RPM_BUILD_ROOT%{_sysconfdir}/monitorix.conf
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf
install -d $RPM_BUILD_ROOT%{_sbindir}
install monitorix.pl $RPM_BUILD_ROOT%{_sbindir}
install -d $RPM_BUILD_ROOT/home/services/httpd/cgi-bin/monitorix
install monitorix.cgi $RPM_BUILD_ROOT/home/services/httpd/cgi-bin
install -d $RPM_BUILD_ROOT%{_datadir}/monitorix
install logo_top.jpg $RPM_BUILD_ROOT%{_datadir}/monitorix
install logo_bot_black.png $RPM_BUILD_ROOT%{_datadir}/monitorix
install logo_bot_white.png $RPM_BUILD_ROOT%{_datadir}/monitorix
install envelope.png $RPM_BUILD_ROOT%{_datadir}/monitorix
install localhost.cgi $RPM_BUILD_ROOT/home/services/httpd/cgi-bin/monitorix
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/reports/ca/imgs_email
install reports/ca/traffic_report.html $RPM_BUILD_ROOT%{_datadir}/%{name}/reports/ca
install reports/ca/traffic_report.sh $RPM_BUILD_ROOT%{_datadir}/%{name}/reports/ca
install reports/ca/imgs_email/blank.png $RPM_BUILD_ROOT%{_datadir}/%{name}/reports/ca/imgs_email
install reports/ca/imgs_email/logo.jpg $RPM_BUILD_ROOT%{_datadir}/%{name}/reports/ca/imgs_email
install reports/ca/imgs_email/signature.png $RPM_BUILD_ROOT%{_datadir}/%{name}/reports/ca/imgs_email
install reports/ca/imgs_email/title.jpg $RPM_BUILD_ROOT%{_datadir}/%{name}/reports/ca/imgs_email
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/reports/en/imgs_email
install reports/en/traffic_report.html $RPM_BUILD_ROOT%{_datadir}/%{name}/reports/en
install reports/en/traffic_report.sh $RPM_BUILD_ROOT%{_datadir}/%{name}/reports/en
install reports/en/imgs_email/blank.png $RPM_BUILD_ROOT%{_datadir}/%{name}/reports/en/imgs_email
install reports/en/imgs_email/logo.jpg $RPM_BUILD_ROOT%{_datadir}/%{name}/reports/en/imgs_email
install reports/en/imgs_email/signature.png $RPM_BUILD_ROOT%{_datadir}/%{name}/reports/en/imgs_email
install reports/en/imgs_email/title.jpg $RPM_BUILD_ROOT%{_datadir}/%{name}/reports/en/imgs_email
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/usage
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/imgs

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add monitorix
%service %{name} restart

%preun
if [ "$1" = "0" ]; then
	%service %{name} stop
	/sbin/chkconfig --del %{name}
fi

%triggerin -- apache1
%webapp_register apache %{_webapp}

%triggerun -- apache1
%webapp_unregister apache %{_webapp}

%triggerin -- apache < 2.2.0, apache-base
%webapp_register httpd %{_webapp}

%triggerun -- apache < 2.2.0, apache-base
%webapp_unregister httpd %{_webapp}

%files
%defattr(644,root,root,755)
%doc COPYING Changelog Configuration.help README
%attr(754,root,root) /etc/rc.d/init.d/monitorix
%{_sysconfdir}/httpd/conf.d/monitorix.conf
%config(noreplace) %{_sysconfdir}/monitorix.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf
%attr(755,root,root) %{_sbindir}/monitorix.pl
%attr(755,root,root) /home/services/httpd/cgi-bin/monitorix.cgi
%attr(755,root,root) /home/services/httpd/cgi-bin/monitorix/localhost.cgi
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/reports
%dir %{_datadir}/%{name}/ca
%dir %{_datadir}/%{name}/ca/imgs_email
%dir %{_datadir}/%{name}/en
%dir %{_datadir}/%{name}/en/imgs_email
%{_datadir}/monitorix/logo_top.jpg
%{_datadir}/monitorix/*.png
%defattr(-, http, http)
%dir %{_datadir}/%{name}/imgs
%config(noreplace) %{_datadir}/%{name}/reports/ca/traffic_report.html
%config(noreplace) %{_datadir}/%{name}/reports/ca/traffic_report.sh
%config(noreplace) %{_datadir}/%{name}/reports/ca/imgs_email/blank.png
%config(noreplace) %{_datadir}/%{name}/reports/ca/imgs_email/logo.jpg
%config(noreplace) %{_datadir}/%{name}/reports/ca/imgs_email/signature.png
%config(noreplace) %{_datadir}/%{name}/reports/ca/imgs_email/title.jpg
%config(noreplace) %{_datadir}/%{name}/reports/en/traffic_report.html
%config(noreplace) %{_datadir}/%{name}/reports/en/traffic_report.sh
%config(noreplace) %{_datadir}/%{name}/reports/en/imgs_email/blank.png
%config(noreplace) %{_datadir}/%{name}/reports/en/imgs_email/logo.jpg
%config(noreplace) %{_datadir}/%{name}/reports/en/imgs_email/signature.png
%config(noreplace) %{_datadir}/%{name}/reports/en/imgs_email/title.jpg
