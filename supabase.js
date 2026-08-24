import { createClient } from
  'https://cdn.jsdelivr.net/npm/@supabase/supabase-js/+esm';

const supabaseUrl = 'https://hmnqssfritstinuczbrb.supabase.co/rest/v1/';
const supabaseKey = 'sb_publishable_dUsMc7XNS73rzs8ZMjMa-w_vcOmUAoh';

export const supabase = createClient(
  supabaseUrl,
  supabaseKey
);
