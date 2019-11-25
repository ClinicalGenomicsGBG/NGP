"""Short validation functions for data structures."""

import re
import json
import click

from cerberus import Validator
import colander
import schema
import voluptuous

# from schema import Schema, And, Use, Optional, Regex
# from voluptuous import Schema, Required, All


def cerberus_validate(struct):
    schema = {'run': {'type': 'string',
                      'regex': '[a-zA-Z]+_[a-zA-Z]+_[a-zA-Z]'},
              'date': {'type': 'string',
                       'regex': '[0-9]{2}[0-1][0-9][0-3][0-9]'},
              'samples': {'type': 'list',
                          'items': [{'type': 'string'}]},
              'metadata': {'type': 'dict',
                           'keysrules': {'type': 'string'}}}

    V = Validator(schema)
    return V.validate(struct)  # Funkar fan inte ens...


def colander_validate(struct):

    class Run(colander.TupleSchema):
        name = colander.SchemaNode(colander.String(),
                                   validator=colander.regex('[a-zA-Z]+_[a-zA-Z]+_[a-zA-Z]'))

    class Data(colander.MappingSchema):
        name = Run()

    # return ???  # Fan är det här för format?


def schema_validate(struct):

    schem = schema.Schema({'run': schema.Regex('[a-zA-Z]+_[a-zA-Z]+_[a-zA-Z]'),
                           'date': schema.Regex('[0-9]{2}[0-1][0-9][0-3][0-9]'),
                           schema.Optional('samples'): schema.And(list),
                           schema.Optional('metadata'): schema.And(dict)})

    validated = schem.validate(struct)
    return validated


def voluptous_validate(struct):
    schema = voluptuous.Schema({
        voluptuous.Required('run'): str,
        'date': str,
        'samples': list,
        'metadata': dict,
        'test': str
    })

    return schema(struct)


def valideer_validate(struct):

    # Har inte uppdaterats på typ 3 år
    pass


def schematics_validate(struct):

    # Verkar lika skit som colander med en massa klasser
    pass


@click.group()
def cli():
    pass


@cli.command()
@click.argument('j_file')
def main(j_file):

    with open(j_file, 'r') as inp:
        data = json.load(inp)

    # Cerberus
    # cerb_val = cerberus_validate(data)
    # print(cerb_val)

    # Colander
    # col_val = colander_validate(data)
    # print(col_val)

    # Schema
    schem_val = schema_validate(data)
    print(schem_val)

    # Voluptuous
    schem_val = voluptous_validate(data)
    print(schem_val)


if __name__ == '__main__':
    cli()
