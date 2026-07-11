%global tl_name texdimens
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Conversion of TeX dimensions to decimals
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/texdimens
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texdimens.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texdimens.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Utilities and documentation related to TeX dimensional units, usable
both with Plain (\input texdimens) and with LaTeX
(\usepackage{texdimens}).

