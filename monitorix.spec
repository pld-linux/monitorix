Summary:	Lightweight system monitoring tool designed to monitorize as many services as it can
Name:		monitorix
Version:	0.8.1
Release:	0.1
License:	GPL
Group:		Applications/System
URL:		http://www.monitorix.org
Source0:	http://www.monitorix.org/%{name}-%{version}.tar.gz
# Source0-md5:	ddd330c84b59ea7ebb7cf63d9031757f
Requires:	bash
Requires:	perl
Requires:	rrdtool
Requires:	webserver
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Monitorix is a free, open source, lightweight system monitoring tool
designed to monitorize as many services as it can. At this time it
monitors from the CPU load and temperatures to the users using the
system. Network devices activity, network services demand and even the
devices' interrupt activity are also monitored.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d ${RPM_BUILD_ROOT}%{_sysconfdir}/rc.d/init.d
install ports/Linux-RHFC/monitorix.init ${RPM_BUILD_ROOT}%{_sysconfdir}/rc.d/init.d/monitorix
install -d ${RPM_BUILD_ROOT}%{_sysconfdir}/httpd/conf.d
install monitorix-apache.conf ${RPM_BUILD_ROOT}%{_sysconfdir}/httpd/conf.d/monitorix.conf
install -d ${RPM_BUILD_ROOT}%{_sysconfdir}
install monitorix.conf ${RPM_BUILD_ROOT}%{_sysconfdir}/monitorix.conf
install -d ${RPM_BUILD_ROOT}%{_sbindir}
install monitorix.pl ${RPM_BUILD_ROOT}%{_sbindir}
install -d ${RPM_BUILD_ROOT}/home/services/httpd/html/monitorix
install logo_top.jpg ${RPM_BUILD_ROOT}/home/services/httpd/html/monitorix
install logo_bot_black.png ${RPM_BUILD_ROOT}/home/services/httpd/html/monitorix
install logo_bot_white.png ${RPM_BUILD_ROOT}/home/services/httpd/html/monitorix
install envelope.png ${RPM_BUILD_ROOT}/home/services/httpd/html/monitorix
install -d ${RPM_BUILD_ROOT}/home/services/httpd/html/monitorix/imgs
install -d ${RPM_BUILD_ROOT}/home/services/httpd/cgi-bin/monitorix
install monitorix.cgi ${RPM_BUILD_ROOT}/home/services/httpd/cgi-bin
install localhost.cgi ${RPM_BUILD_ROOT}/home/services/httpd/cgi-bin/monitorix
install -d ${RPM_BUILD_ROOT}/var/lib/monitorix/reports/ca/imgs_email
install reports/ca/traffic_report.html ${RPM_BUILD_ROOT}/var/lib/monitorix/reports/ca
install reports/ca/traffic_report.sh ${RPM_BUILD_ROOT}/var/lib/monitorix/reports/ca
install reports/ca/imgs_email/blank.png ${RPM_BUILD_ROOT}/var/lib/monitorix/reports/ca/imgs_email
install reports/ca/imgs_email/logo.jpg ${RPM_BUILD_ROOT}/var/lib/monitorix/reports/ca/imgs_email
install reports/ca/imgs_email/signature.png ${RPM_BUILD_ROOT}/var/lib/monitorix/reports/ca/imgs_email
install reports/ca/imgs_email/title.jpg ${RPM_BUILD_ROOT}/var/lib/monitorix/reports/ca/imgs_email
install -d ${RPM_BUILD_ROOT}/var/lib/monitorix/reports/en/imgs_email
install reports/en/traffic_report.html ${RPM_BUILD_ROOT}/var/lib/monitorix/reports/en
install reports/en/traffic_report.sh ${RPM_BUILD_ROOT}/var/lib/monitorix/reports/en
install reports/en/imgs_email/blank.png ${RPM_BUILD_ROOT}/var/lib/monitorix/reports/en/imgs_email
install reports/en/imgs_email/logo.jpg ${RPM_BUILD_ROOT}/var/lib/monitorix/reports/en/imgs_email
install reports/en/imgs_email/signature.png ${RPM_BUILD_ROOT}/var/lib/monitorix/reports/en/imgs_email
install reports/en/imgs_email/title.jpg ${RPM_BUILD_ROOT}/var/lib/monitorix/reports/en/imgs_email
install -d ${RPM_BUILD_ROOT}/var/lib/monitorix/usage

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add monitorix
mkdir -p /home/services/httpd/html/monitorix/imgs
mkdir -p /var/lib/monitorix/usage
chown apache:apache /home/services/httpd/html/monitorix/imgs

%files
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/monitorix
%{_sysconfdir}/httpd/conf.d/monitorix.conf
%config(noreplace) %{_sysconfdir}/monitorix.conf
%attr(755,root,root) %{_sbindir}/monitorix.pl
%defattr(-, apache, apache)
/home/services/httpd/html/monitorix/logo_top.jpg
/home/services/httpd/html/monitorix/logo_bot_black.png
/home/services/httpd/html/monitorix/logo_bot_white.png
/home/services/httpd/html/monitorix/envelope.png
/home/services/httpd/cgi-bin/monitorix.cgi
/home/services/httpd/cgi-bin/monitorix/localhost.cgi
%config(noreplace) /var/lib/monitorix/reports/ca/traffic_report.html
%config(noreplace) /var/lib/monitorix/reports/ca/traffic_report.sh
%config(noreplace) /var/lib/monitorix/reports/ca/imgs_email/blank.png
%config(noreplace) /var/lib/monitorix/reports/ca/imgs_email/logo.jpg
%config(noreplace) /var/lib/monitorix/reports/ca/imgs_email/signature.png
%config(noreplace) /var/lib/monitorix/reports/ca/imgs_email/title.jpg
%config(noreplace) /var/lib/monitorix/reports/en/traffic_report.html
%config(noreplace) /var/lib/monitorix/reports/en/traffic_report.sh
%config(noreplace) /var/lib/monitorix/reports/en/imgs_email/blank.png
%config(noreplace) /var/lib/monitorix/reports/en/imgs_email/logo.jpg
%config(noreplace) /var/lib/monitorix/reports/en/imgs_email/signature.png
%config(noreplace) /var/lib/monitorix/reports/en/imgs_email/title.jpg
%doc COPYING Changelog Configuration.help README
