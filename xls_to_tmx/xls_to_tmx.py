import html

from .constants import (
  FOOTER, 
  HEADER, 
  TU,
)

from .utils import (
  get_outputtmxfilepath,
  get_complete_kwargs,
  show_progress,
  get_sh_maxrows_cell_value
)


def convert(filepath, **kwargs):
  
  max_rows, cell_value, start_row, col = get_sh_maxrows_cell_value(filepath)

  output_tmx_filepath = get_outputtmxfilepath(filepath)
  kwargs = get_complete_kwargs(**kwargs)

  with open(output_tmx_filepath, mode='a', encoding='utf-8') as f:

    f.write(HEADER.format(**kwargs))

    for row in range(start_row, max_rows):
        try:
          kwargs['source_seg'] = html.escape(cell_value(row, col))
          kwargs['target_seg'] = html.escape(cell_value(row, col))
            
        except IndexError as e:
          pass

        f.write(TU.format(**kwargs))
        show_progress(row)

    f.write(FOOTER)
    print('Saved to ' + str(output_tmx_filepath))


if __name__=='__main__':
  pass
