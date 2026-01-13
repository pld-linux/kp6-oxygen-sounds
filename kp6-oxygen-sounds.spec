#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	6.5.5
%define		qtver		5.15.2
%define		kpname		oxygen-sounds
Summary:	Sound files for Plasma
Summary(pl.UTF-8):	Pliki dżwiękowe dla Plasmy
Name:		kp6-%{kpname}
Version:	6.5.5
Release:	1
License:	BSD-2-Clause/CC-BY-3.0/CC0-1.0/LGPL-3.0-or-later
Group:		X11/Applications/Sound
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	865ba29838609c935803a8d0cb8399c1
URL:		http://www.kde.org/
BuildRequires:	cmake >= 3.16.0
BuildRequires:	kf6-extra-cmake-modules >= 1.4.0
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Obsoletes:	kp5-%{kpname} < 6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sound files for Plasma.

%description -l pl.UTF-8
Pliki dżwiękowe dla Plasmy.

%prep
%setup -q -n %{kpname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DBUILD_QT5=OFF \
	-DBUILD_QT6=ON
%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/sounds/Oxygen-Im-Cant-Connect.ogg
%{_datadir}/sounds/Oxygen-Im-Connection-Lost.ogg
%{_datadir}/sounds/Oxygen-Im-Contact-In.ogg
%{_datadir}/sounds/Oxygen-Im-Contact-Out.ogg
%{_datadir}/sounds/Oxygen-Im-Error-On-Connection.ogg
%{_datadir}/sounds/Oxygen-Im-Highlight-Msg.ogg
%{_datadir}/sounds/Oxygen-Im-Internal-Error.ogg
%{_datadir}/sounds/Oxygen-Im-Irc-Event.ogg
%{_datadir}/sounds/Oxygen-Im-Low-Priority-Message.ogg
%{_datadir}/sounds/Oxygen-Im-Message-In.ogg
%{_datadir}/sounds/Oxygen-Im-Message-Out.ogg
%{_datadir}/sounds/Oxygen-Im-Network-Problems.ogg
%{_datadir}/sounds/Oxygen-Im-New-Mail.ogg
%{_datadir}/sounds/Oxygen-Im-Nudge.ogg
%{_datadir}/sounds/Oxygen-Im-Phone-Ring.ogg
%{_datadir}/sounds/Oxygen-Im-Sms.ogg
%{_datadir}/sounds/Oxygen-Im-User-Auth.ogg
%{_datadir}/sounds/Oxygen-K3B-Finish-Error.ogg
%{_datadir}/sounds/Oxygen-K3B-Finish-Success.ogg
%{_datadir}/sounds/Oxygen-K3B-Insert-Medium.ogg
%{_datadir}/sounds/Oxygen-Sys-App-Error-Critical.ogg
%{_datadir}/sounds/Oxygen-Sys-App-Error-Serious-Very.ogg
%{_datadir}/sounds/Oxygen-Sys-App-Error-Serious.ogg
%{_datadir}/sounds/Oxygen-Sys-App-Error.ogg
%{_datadir}/sounds/Oxygen-Sys-App-Message.ogg
%{_datadir}/sounds/Oxygen-Sys-App-Negative.ogg
%{_datadir}/sounds/Oxygen-Sys-App-Positive.ogg
%{_datadir}/sounds/Oxygen-Sys-Error-Printing.ogg
%{_datadir}/sounds/Oxygen-Sys-File-Open-Foes.ogg
%{_datadir}/sounds/Oxygen-Sys-List-End.ogg
%{_datadir}/sounds/Oxygen-Sys-List-Match-Multiple.ogg
%{_datadir}/sounds/Oxygen-Sys-List-Match-No.ogg
%{_datadir}/sounds/Oxygen-Sys-Log-In-Long.ogg
%{_datadir}/sounds/Oxygen-Sys-Log-In-Short.ogg
%{_datadir}/sounds/Oxygen-Sys-Log-In.ogg
%{_datadir}/sounds/Oxygen-Sys-Log-Out-Long.ogg
%{_datadir}/sounds/Oxygen-Sys-Log-Out.ogg
%{_datadir}/sounds/Oxygen-Sys-Question.ogg
%{_datadir}/sounds/Oxygen-Sys-Special.ogg
%{_datadir}/sounds/Oxygen-Sys-Trash-Emptied.ogg
%{_datadir}/sounds/Oxygen-Sys-Warning.ogg
%{_datadir}/sounds/Oxygen-Window-All-Desktops-Not.ogg
%{_datadir}/sounds/Oxygen-Window-All-Desktops.ogg
%{_datadir}/sounds/Oxygen-Window-Close.ogg
%{_datadir}/sounds/Oxygen-Window-Maximize.ogg
%{_datadir}/sounds/Oxygen-Window-Minimize.ogg
%{_datadir}/sounds/Oxygen-Window-Move-Stop.ogg
%{_datadir}/sounds/Oxygen-Window-Move.ogg
%{_datadir}/sounds/Oxygen-Window-Shade-Down.ogg
%{_datadir}/sounds/Oxygen-Window-Shade-Up.ogg
%{_datadir}/sounds/oxygen
