%define		_font_name	Nafees_Nastaleeq
Summary:	Free fonts from Center for Research in Urdu Language Processing
Summary(pl.UTF-8):	Wolnodostępne czcionki z Centrum Badań nad Przetwarzaniem Języka Urdu
Name:		fonts-TTF-CRULP-Nafees_Nastaleeq
Version:	1.02
Release:	0.1
License:	MPL-like
Group:		Fonts
Source0:	http://www.crulp.org/Downloads/localization/fonts/NafeesNastaleeq/%{_font_name}_v%{version}.zip
# Source0-md5:	34ca164ce011b682522431fc332c0cb6
URL:		http://www.crulp.org/software/localization/Fonts/nafeesNastaleeq.html
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF

%description
Nafees Nastaleeq is developed according to calligraphic rules, following the style
of Syed Nafees Al-Hussaini (Nafees Raqam), one of the finest calligraphers of
Pakistan. Guidance and calligraphy of basic glyphs for the font has been provided
by Syed Jameel-ur-Rehman. He is pupil of Syed Nafees Shah and Hafiz
Syed Anees-ul-Hassan.

%prep
%setup -q -c %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ttffontsdir}

install *.ttf $RPM_BUILD_ROOT%{ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc %{_font_name}_v%{version}.pdf
%{ttffontsdir}/*.ttf
