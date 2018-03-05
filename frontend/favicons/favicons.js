/* File used to link the favicons imgs to the built webpack's pack */

const faviconsContext = require.context(
    /*  inline loader to force all the favicons files to be bundled in the chosen folder.  */
  '!!file-loader?name=static/app/assets/favicons/[name].[ext]!.', 
  true,
  /\.(svg|png|ico|xml|json)$/
);

faviconsContext.keys().forEach(faviconsContext);