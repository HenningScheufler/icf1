/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     |
    \\  /    A nd           | www.openfoam.com
     \\/     M anipulation  |
-------------------------------------------------------------------------------
    Copyright (C) 2019 OpenCFD Ltd.
    Copyright (C) 2019-2020 DLR
-------------------------------------------------------------------------------
License
    This file is part of OpenFOAM.

    OpenFOAM is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    OpenFOAM is distributed in the hope that it will be useful, but WITHOUT
    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
    FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
    for more details.

    You should have received a copy of the GNU General Public License
    along with OpenFOAM.  If not, see <http://www.gnu.org/licenses/>.

Class
    Foam::implicitFunctions::ellipsoidImpFunction

Description
    creates an ellipsoidImpFunction

    Original code supplied by Henning Scheufler, DLR (2019)

SourceFiles
    ellipsoidImpFunction.C

\*---------------------------------------------------------------------------*/

#ifndef implicitFunction_ellipsoidImpFunction_H
#define implicitFunction_ellipsoidImpFunction_H

#include "implicitFunction.H"
#include "mathematicalConstants.H"

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

namespace Foam
{
namespace implicitFunctions
{

/*---------------------------------------------------------------------------*\
                  Class ellipsoidImpFunction Declaration
\*---------------------------------------------------------------------------*/

class ellipsoidImpFunction
:
    public implicitFunction
{
    // Private Member Data

        //- Axis
        const vector semiAxis_;

        //- Origin point
        const vector origin_;


public:

    //- Runtime type information
    TypeName("ellipsoid");


    // Constructors

        //- Construct from components
        explicit ellipsoidImpFunction
        (
            const vector& semiAxis,
            const vector& origin
        );

        //- Construct from dictionary
        explicit ellipsoidImpFunction(const dictionary& dict);


    //- Destructor
    virtual ~ellipsoidImpFunction() = default;


    // Member Functions

    virtual scalar value(const vector& p) const
    {
        return
           -sqrt
            (
                sqr((p.x() - origin_.x())/semiAxis_.x())
              + sqr((p.y() - origin_.y())/semiAxis_.y())
              + sqr((p.z() - origin_.z())/semiAxis_.z())
            ) + 1;
    }


    virtual vector grad(const vector& p) const
    {
        // normal_ has the length of one
        return vector
        (
            2*(p.x() - origin_.x())/sqr(semiAxis_.x()),
            2*(p.y() - origin_.y())/sqr(semiAxis_.y()),
            2*(p.z() - origin_.z())/sqr(semiAxis_.z())
        );
    }

    virtual scalar distanceToSurfaces(const vector& p) const
    {
        NotImplemented;
        return GREAT;
    }
};


// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

} // End namespace implicitFunctions
} // End namespace Foam

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

#endif

// ************************************************************************* //
