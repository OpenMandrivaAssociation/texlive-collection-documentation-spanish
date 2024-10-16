# revision 19634
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-documentation-spanish
Epoch:		1
Version:	20120224
Release:	11
Summary:	Spanish documentation
Group:		Publishing
URL:		https://tug.org/texlive
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


%changelog
* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120224-1
+ Revision: 780274
- Update to latest release.
- Import texlive-collection-documentation-spanish
- Import texlive-collection-documentation-spanish

