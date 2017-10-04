# helpers for showing signals

import matplotlib.pyplot as plt


def show(ticker, signals, returns, ma=None, strat=None, ax=None, title=None, legend=True):
    if ax is None:
        _, axes = plt.subplots(1, 1, figsize=(10, 6));
        ax = axes

    # show returns
    (returns[ticker]
            .dropna()
            .cumsum()
            .rename(ticker)
            .plot
            .line(ax=ax, legend=legend)
     )

    # moving avg
    if ma is not None:
        (ma[ticker]
         .dropna()
         .cumsum()
         .rename('%s 50d MA' % ticker)
         .plot
         .line(ax=ax, legend=legend)
         )

    # show signals
    s = signals[ticker]
    (s.where(s>0)
      .rename('signal buy')
      .plot
      .line(ax=ax, secondary_y=True, color='pink', alpha=0.5, legend=legend)
     )
    (s.where(s<0)
      .rename('signal sell')
      .plot
      .line(ax=ax, secondary_y=True, color='purple', alpha=0.5, legend=legend)
     )


    # show strategy
    if strat is not None:
        (strat[ticker]
         .dropna()
         .cumsum()
         .rename('%s Strategy' % ticker)
         .plot
         .line(ax=ax, legend=legend)
         )

    if title is not None:
        ax.set_title(title)
