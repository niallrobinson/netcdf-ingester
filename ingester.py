import iris
iris.FUTURE.cell_datetime_objects


def gen_key(cube, coords):
    """
    Combine the coordinates from a cube to give
    uid key string

    """
    key = cube.name().replace("_", "-").replace(" ", "-")
    for coord in coords:    
        this_point = str(cube.coord(coord).cell(0).point).replace(" ", "-")
        key += "_"
        key += this_point
    return key


def slice_cube(cube):
    """
    Slices a n-dimensional cube into a series of lat lon cubes

    Returns:
        * a dictionary of uid key: cubes for each chunks
        * a list of the values which have been combined
            to make the uid keys. Values are in order
            and separated by underscores. All spaces and
            underscores in component values have been
            coverted to hyphens.

    """
    [x_coord] = cube.coords(axis="X", dim_coords=True)
    [y_coord] = cube.coords(axis="Y", dim_coords=True)
    other_coords = [c for c in cube.coords(dim_coords=True) if c != x_coord and c != y_coord]

    slices = {}
    for c in cube.slices([x_coord, y_coord]):
        slices[gen_key(c, other_coords)] = c

    keys = ["variable_name"]
    keys.extend([c.name() for c in other_coords])

    return slices, keys


if __name__=='__main__':
    pass