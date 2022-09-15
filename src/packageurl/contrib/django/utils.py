# -*- coding: utf-8 -*-
#
# Copyright (c) the purl authors
# SPDX-License-Identifier: MIT
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Visit https://github.com/package-url/packageurl-python for support and
# download.


from packageurl import PackageURL


def purl_to_lookups(purl, encode=True):
    """
    Return a lookups dict built from the provided `purl` string.
    Those lookups can be used as QuerySet filters.
    """
    if not purl.startswith("pkg:"):
        purl = "pkg:" + purl

    try:
        package_url = PackageURL.from_string(purl)
    except ValueError:
        return  # Not a valid PackageURL

    package_url_dict = package_url.to_dict(encode=encode)
    return without_empty_values(package_url_dict)


def without_empty_values(input_dict):
    """
    Return a new dict not including empty value entries from `input_dict`.

    `None`, empty string, empty list, and empty dict/set are cleaned.
    `0` and `False` values are kept.
    """
    empty_values = ([], (), {}, "", None)

    return {key: value for key, value in input_dict.items() if value not in empty_values}
