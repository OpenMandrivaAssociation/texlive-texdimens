Name:		texlive-texdimens
Version:	61070
Release:	2
Summary:	Conversion of TeX dimensions to decimals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/texdimens
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texdimens.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texdimens.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Utilities and documentation related to TeX dimensional units,
usable both with Plain (\input texdimens) and with LaTeX
(\usepackage{texdimens}).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/generic/texdimens
%doc %{_texmfdistdir}/doc/generic/texdimens

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
