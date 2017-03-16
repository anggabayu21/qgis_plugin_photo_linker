# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PhotoLinker
                                 A QGIS plugin
 Photo linker links points to photos
                             -------------------
        begin                : 2017-03-16
        copyright            : (C) 2017 by Bayu
        email                : anggabayu@ait.asia
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load PhotoLinker class from file PhotoLinker.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .photo_linker import PhotoLinker
    return PhotoLinker(iface)
