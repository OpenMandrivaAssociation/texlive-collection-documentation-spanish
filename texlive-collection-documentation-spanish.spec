# revision 19634
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-documentation-spanish
Version:	20120223
Release:	1
Summary:	Spanish documentation
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-documentation-spanish.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-es-tex-faq
Requires:	texlive-l2tabu-spanish
Requires:	texlive-latex2e-help-texinfo-spanish
Requires:	texlive-latexcheat-esmx
Requires:	texlive-lshort-spanish
Requires:	texlive-collection-documentation-base

%description
TeXLive collection-documentation-spanish package.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
